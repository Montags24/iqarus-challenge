function checkLocationPermission () {
  if ('permissions' in navigator && 'geolocation' in navigator) {
    // Check if permission is already granted
    navigator.permissions.query({ name: 'geolocation' }).then(function (permissionStatus) {
      if (permissionStatus.state === 'granted') {
        // Permission already granted, get the user's location
        getLocation()
      } else {
        // Permission not granted, ask the user for permission
        navigator.geolocation.getCurrentPosition(getLocation, function (error) {
          console.error('Error getting location:', error)
        })
      }
    })
  } else if ('geolocation' in navigator) {
    // Geolocation is available but permissions API is not supported
    getLocation()
  } else {
    // Geolocation is not available
    console.error('Geolocation is not supported by this browser.')
  }
}

function getLocation () {
  navigator.geolocation.getCurrentPosition(
    function (position) {
      const latitude = position.coords.latitude
      const longitude = position.coords.longitude

      console.log('Latitude:', latitude)
      console.log('Longitude:', longitude)

      // You can now use latitude and longitude in your application
    },
    function (error) {
      // Handle any errors that occur when trying to get the user's location
      console.error('Error getting location:', error)
    }
  )
}

export { checkLocationPermission }
