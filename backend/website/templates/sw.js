if (!self.define) {
  let e,
    i = {}
  const n = (n, r) => (
    (n = new URL(n + '.js', r).href),
    i[n] ||
      new Promise(i => {
        if ('document' in self) {
          const e = document.createElement('script')
          ;(e.src = n), (e.onload = i), document.head.appendChild(e)
        } else (e = n), importScripts(n), i()
      }).then(() => {
        let e = i[n]
        if (!e) throw new Error(`Module ${n} didn’t register its module`)
        return e
      })
  )
  self.define = (r, s) => {
    const t =
      e ||
      ('document' in self ? document.currentScript.src : '') ||
      location.href
    if (i[t]) return
    let o = {}
    const c = e => n(e, t),
      d = { module: { uri: t }, exports: o, require: c }
    i[t] = Promise.all(r.map(e => d[e] || c(e))).then(e => (s(...e), o))
  }
}
define(['./workbox-3e911b1d'], function (e) {
  'use strict'
  self.skipWaiting(),
    e.clientsClaim(),
    e.precacheAndRoute(
      [
        { url: 'assets/index-BVZvcXuB.css', revision: null },
        { url: 'index.html', revision: '247003c87e20f6f33b0f3d888a6bb550' },
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
//# sourceMappingURL=sw.js.map
