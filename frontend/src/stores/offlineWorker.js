// Open a connection to the IndexedDB database
const dbName = 'offlineDB'
const dbVersion = 1
let db

// Function to open a connection to the IndexedDB
const openDB = dbHeader => {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open(dbName, dbVersion)

    request.onerror = event => {
      reject('Error opening IndexedDB database: ' + event.target.errorCode)
    }

    request.onsuccess = event => {
      db = event.target.result
      resolve()
    }

    request.onupgradeneeded = event => {
      db = event.target.result
      if (!db.objectStoreNames.contains(dbHeader)) {
        const objectStore = db.createObjectStore(dbHeader, {
          keyPath: 'id',
          autoIncrement: true
        })
        objectStore.createIndex('name', 'name', { unique: false })
      }
    }
  })
}

// Function to add an item to the IndexedDB
const addItem = async (name, dbHeader) => {
  try {
    await openDB(dbHeader)
    return new Promise((resolve, reject) => {
      const transaction = db.transaction([dbHeader], 'readwrite')
      const store = transaction.objectStore(dbHeader)
      const newItem = { name }
      const request = store.add(newItem)

      request.onerror = event => {
        reject('Error adding item to IndexedDB: ' + event.target.errorCode)
      }

      request.onsuccess = event => {
        resolve(event.target.result)
      }
      transaction.oncomplete = () => {
        db.close() // Optional: close the database after transaction completes
      }
    })
  } catch (error) {
    console.log('am ghere')
    console.error(error)
  }
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
