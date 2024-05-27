const dbName = 'offlineDB'
const dbVersion = 1
let db

// Function to open a connection to the IndexedDB and ensure the object stores exist
const openDB = () => {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open(dbName, dbVersion)

    request.onerror = event => {
      reject('Error opening IndexedDB database: ' + event.target.errorCode)
    }

    request.onsuccess = event => {
      db = event.target.result
      resolve(db)
    }

    request.onupgradeneeded = event => {
      const db = event.target.result
      if (!db.objectStoreNames.contains('sessionJwt')) {
        db.createObjectStore('sessionJwt', { keyPath: 'id', autoIncrement: true })
      }
      if (!db.objectStoreNames.contains('formEntries')) {
        db.createObjectStore('formEntries', { keyPath: 'id', autoIncrement: true })
      }
    }
  })
}

// Function to add an item to the specified object store
const addItem = async (item, storeName) => {
  console.log(item)
  try {
    const db = await openDB()
    return new Promise((resolve, reject) => {
      const transaction = db.transaction([storeName], 'readwrite')
      const store = transaction.objectStore(storeName)
      if (item.id) {
        delete item.id
      }
      const request = store.add(item)

      request.onerror = event => {
        reject('Error adding item to IndexedDB: ' + event.target.errorCode)
      }

      request.onsuccess = event => {
        resolve(event.target.result)
      }

      transaction.oncomplete = () => {
        db.close() // Close the database after transaction completes
      }
    })
  } catch (error) {
    throw new Error('Failed to add item to database: ' + error.message)
  }
}

// Function to get all items from the specified object store
const getAllItems = async storeName => {
  try {
    const db = await openDB()
    return new Promise((resolve, reject) => {
      const transaction = db.transaction([storeName], 'readonly')
      const store = transaction.objectStore(storeName)
      const request = store.getAll()

      request.onerror = event => {
        reject('Error fetching items from IndexedDB: ' + event.target.errorCode)
      }

      request.onsuccess = event => {
        resolve(event.target.result)
      }

      transaction.oncomplete = () => {
        db.close() // Close the database after transaction completes
      }
    })
  } catch (error) {
    throw new Error('Failed to fetch items from database: ' + error.message)
  }
}

// Function to clear all items from the specified object store
const clearStore = async storeName => {
  try {
    const db = await openDB()
    return new Promise((resolve, reject) => {
      const transaction = db.transaction([storeName], 'readwrite')
      const store = transaction.objectStore(storeName)
      const request = store.clear()

      request.onerror = event => {
        reject('Error clearing store in IndexedDB: ' + event.target.errorCode)
      }

      request.onsuccess = event => {
        resolve()
      }

      transaction.oncomplete = () => {
        db.close() // Close the database after transaction completes
      }
    })
  } catch (error) {
    throw new Error('Failed to clear store in database: ' + error.message)
  }
}

export { addItem, getAllItems, clearStore }
