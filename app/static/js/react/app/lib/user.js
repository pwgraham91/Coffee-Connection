export function isCurrentUser(userID) {
  return window.user && parseInt(userID) === parseInt(window.user.id)
}

export function getNameInitials(name) {
  let initials = ''
  for (let i = 0; i < name.length; i++) {
    const previousIndex = i - 1
    if (previousIndex < 0 || name[previousIndex] === ' ') {
      initials += name[i]
    }
  }
  return initials
}
