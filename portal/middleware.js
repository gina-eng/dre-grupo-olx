// Portão de senha do portal. Roda no edge da Vercel, antes de qualquer arquivo estático.
// A senha vive na variável de ambiente PORTAL_SENHA do projeto — nunca no repositório.
export const config = {
  matcher: '/((?!_vercel|favicon\\.ico).*)',
}

const REALM = 'Portal DR-E Grupo OLX'

function desafio() {
  return new Response(
    'Acesso restrito. Este portal contém informação confidencial do Grupo OLX.',
    {
      status: 401,
      headers: {
        'WWW-Authenticate': `Basic realm="${REALM}", charset="UTF-8"`,
        'Content-Type': 'text/plain; charset=utf-8',
        'Cache-Control': 'no-store',
      },
    }
  )
}

// Comparação de tempo constante: não vaza o tamanho nem o prefixo da senha.
function iguais(a, b) {
  const ea = new TextEncoder().encode(a)
  const eb = new TextEncoder().encode(b)
  let dif = ea.length ^ eb.length
  const n = Math.max(ea.length, eb.length)
  for (let i = 0; i < n; i++) dif |= (ea[i] ?? 0) ^ (eb[i] ?? 0)
  return dif === 0
}

export default function middleware(request) {
  const esperada = process.env.PORTAL_SENHA
  if (!esperada) {
    return new Response('PORTAL_SENHA não configurada no projeto.', {
      status: 500,
      headers: { 'Content-Type': 'text/plain; charset=utf-8', 'Cache-Control': 'no-store' },
    })
  }

  const cabecalho = request.headers.get('authorization') || ''
  const [esquema, codificado] = cabecalho.split(' ')
  if (esquema !== 'Basic' || !codificado) return desafio()

  let decodificado
  try {
    decodificado = atob(codificado)
  } catch {
    return desafio()
  }

  const sep = decodificado.indexOf(':')
  const senha = sep === -1 ? '' : decodificado.slice(sep + 1)
  if (!iguais(senha, esperada)) return desafio()

  // Autenticado: segue para o arquivo estático.
  return undefined
}
