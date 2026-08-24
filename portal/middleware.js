// Portão de acesso do portal. Roda no edge da Vercel, antes de qualquer arquivo estático.
// Os pares usuário/senha vivem na variável de ambiente PORTAL_CREDENCIAIS do projeto,
// no formato "usuario:senha,usuario:senha". Nunca no repositório.
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

// Comparação de tempo constante: não vaza o tamanho nem o prefixo do segredo.
function iguais(a, b) {
  const ea = new TextEncoder().encode(a)
  const eb = new TextEncoder().encode(b)
  let dif = ea.length ^ eb.length
  const n = Math.max(ea.length, eb.length)
  for (let i = 0; i < n; i++) dif |= (ea[i] ?? 0) ^ (eb[i] ?? 0)
  return dif === 0
}

function credenciais() {
  const bruto = process.env.PORTAL_CREDENCIAIS || ''
  return bruto
    .split(',')
    .map(par => par.trim())
    .filter(Boolean)
    .map(par => {
      const i = par.indexOf(':')
      return i === -1 ? null : { usuario: par.slice(0, i), senha: par.slice(i + 1) }
    })
    .filter(Boolean)
}

export default function middleware(request) {
  const validas = credenciais()
  if (!validas.length) {
    return new Response('PORTAL_CREDENCIAIS não configurada no projeto.', {
      status: 500,
      headers: { 'Content-Type': 'text/plain; charset=utf-8', 'Cache-Control': 'no-store' },
    })
  }

  const cabecalho = request.headers.get('authorization') || ''
  const [esquema, codificado] = cabecalho.split(' ')
  if (esquema !== 'Basic' || !codificado) return desafio()

  // atob devolve latin-1; o par precisa ser relido como UTF-8, senão qualquer
  // caractere acentuado é comparado errado (o header anuncia charset="UTF-8").
  let decodificado
  try {
    const bytes = Uint8Array.from(atob(codificado), c => c.charCodeAt(0))
    decodificado = new TextDecoder('utf-8').decode(bytes)
  } catch {
    return desafio()
  }

  const sep = decodificado.indexOf(':')
  if (sep === -1) return desafio()
  const usuario = decodificado.slice(0, sep)
  const senha = decodificado.slice(sep + 1)

  // Percorre todas as credenciais mesmo após encontrar a certa, para o tempo de
  // resposta não revelar qual usuário existe.
  let ok = false
  for (const c of validas) {
    if (iguais(usuario, c.usuario) & iguais(senha, c.senha)) ok = true
  }
  if (!ok) return desafio()

  return undefined
}
