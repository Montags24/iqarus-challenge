if (!self.define) {
  let e,
    i = {}
  const s = (s, n) => (
    (s = new URL(s + '.js', n).href),
    i[s] ||
      new Promise(i => {
        if ('document' in self) {
          const e = document.createElement('script')
          ;(e.src = s), (e.onload = i), document.head.appendChild(e)
        } else (e = s), importScripts(s), i()
      }).then(() => {
        let e = i[s]
        if (!e) throw new Error(`Module ${s} didn’t register its module`)
        return e
      })
  )
  self.define = (n, r) => {
    const t =
      e ||
      ('document' in self ? document.currentScript.src : '') ||
      location.href
    if (i[t]) return
    let o = {}
    const d = e => s(e, t),
      l = { module: { uri: t }, exports: o, require: d }
    i[t] = Promise.all(n.map(e => l[e] || d(e))).then(e => (r(...e), o))
  }
}
define(['./workbox-3e911b1d'], function (e) {
  'use strict'
  self.skipWaiting(),
    e.clientsClaim(),
    e.precacheAndRoute(
      [
        { url: 'assets/index-C4kIkSwK.js', revision: null },
        { url: 'assets/index-DJ64wXaj.css', revision: null },
        { url: 'index.html', revision: '3c732a617e37f0d7cb3f46d78de53214' },
        { url: 'registerSW.js', revision: '1872c500de691dce40960bb85481de07' },
        {
          url: 'pwa-192x192.png',
          revision: 'e0e5a2a03e5e7c453b16d2cc811ca365'
        },
        {
          url: 'pwa-512x512.png',
          revision: '157410f8328fb8d4e673f8327af3a36d'
        },
        {
          url: 'pwa-maskable-192x192.png',
          revision: '17ccdfe56a38596dbd2d797cac01a370'
        },
        {
          url: 'pwa-maskable-512x512.png',
          revision: '6041b15bba38237e2860a5453bb9b2bc'
        },
        {
          url: 'manifest.webmanifest',
          revision: 'e8112eaef0db81322b97ae1f5b498f6a'
        }
      ],
      {}
    ),
    e.cleanupOutdatedCaches(),
    e.registerRoute(
      new e.NavigationRoute(e.createHandlerBoundToURL('index.html'))
    )
})
