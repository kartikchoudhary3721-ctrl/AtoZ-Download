// Version badal diya taaki mobile purani memory delete kar de
const CACHE_NAME = 'atoz-downloader-cache-v2'; 
const urlsToCache = [
  '/',
  '/manifest.json'
];

// Install Naya Service Worker aur purane ko force replace karo
self.addEventListener('install', event => {
  self.skipWaiting(); 
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(urlsToCache);
    })
  );
});

// Purana Kachra (Cache-v1) Saaf Karo
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cache => {
          if (cache !== CACHE_NAME) {
            return caches.delete(cache);
          }
        })
      );
    })
  );
});

// 🔥 NETWORK FIRST STRATEGY 🔥
// Ye hamesha pehle naya design layega. Agar net band hua, tabhi purana memory use karega.
self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  event.respondWith(
    fetch(event.request).catch(() => caches.match(event.request))
  );
});