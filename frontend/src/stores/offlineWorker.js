// Open a connection to the IndexedDB database
const dbName = 'offlineDB'
const dbVersion = 1
let db

const openDB = () => {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open(dbName, dbVersion)

    request.onerror = event => {
      reject('Error opening IndexedDB database')
    }

    request.onsuccess = event => {
      db = event.target.result
      resolve()
    }

    request.onupgradeneeded = event => {
      db = event.target.result
      const objectStore = db.createObjectStore('items', { keyPath: 'id', autoIncrement: true })
      objectStore.createIndex('name', 'name', { unique: false })
    }
  })
}

// Add an item to the IndexedDB database
const addItem = async name => {
  await openDB()
  return new Promise((resolve, reject) => {
    const transaction = db.transaction(['items'], 'readwrite')
    const store = transaction.objectStore('items')
    const newItem = { name }
    const request = store.add(newItem)

    request.onerror = event => {
      reject('Error adding item to IndexedDB')
    }

    request.onsuccess = event => {
      resolve(event.target.result)
    }
  })
}

// Remove an item from the IndexedDB database
const removeItem = async id => {
  await openDB()
  return new Promise((resolve, reject) => {
    const transaction = db.transaction(['items'], 'readwrite')
    const store = transaction.objectStore('items')
    const request = store.delete(id)

    request.onerror = event => {
      reject('Error removing item from IndexedDB')
    }

    request.onsuccess = event => {
      resolve()
    }
  })
}

// Fetch all items from the IndexedDB database
const getAllItems = async () => {
  await openDB()
  return new Promise((resolve, reject) => {
    const transaction = db.transaction(['items'], 'readonly')
    const store = transaction.objectStore('items')
    const request = store.getAll()

    request.onerror = event => {
      reject('Error fetching items from IndexedDB')
    }

    request.onsuccess = event => {
      resolve(event.target.result)
    }
  })
}

export { addItem, removeItem, getAllItems }
