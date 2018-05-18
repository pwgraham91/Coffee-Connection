import PropTypes from 'prop-types';
import React from 'react';
import Chip from '@material-ui/core/Chip';
import Avatar from '@material-ui/core/Avatar';
import { Redirect } from 'react-router-dom';

export default class Connection extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      navigateTo: undefined
    }
    this.navigateToUser = this.navigateToUser.bind(this);
  }

  renderAvatar(user) {
    if (user.avatar) {
      return (
        <Avatar src={user.avatar} />
      )
    } else {
      return <Avatar>{this.getNameInitials(user.name)}</Avatar>
    }
  }

  getNameInitials(name) {
    let initials = ''
    for (let i = 0; i < name.length; i++) {
      const previousIndex = i - 1
      if (previousIndex < 0 || name[previousIndex] === ' ') {
        initials += name[i]
      }
    }
    return initials
  }

  render() {
      if (this.state.navigateTo) {
        return (
          <Redirect to={this.state.navigateTo} />
        )
      } else {
        return (
          <Chip
            avatar={this.renderAvatar(this.props.user)}
            label={this.props.user.name}
            onClick={() => this.navigateToUser(this.props.user.id)}
          />
        )
      }
  }

  navigateToUser(userId) {
    this.setState({
      navigateTo: `/profile/${userId}`
    })
  }
}

// Connection.propTypes = {
//   userID: PropTypes.string,
//   userDetails: PropTypes.object
// };
