export function isCurrentUser(userID) {
  return window.user && parseInt(userID) === parseInt(window.user.id)
}
