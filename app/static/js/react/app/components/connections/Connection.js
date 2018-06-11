import PropTypes from 'prop-types';
import React from 'react';
import Chip from '@material-ui/core/Chip';
import Avatar from '@material-ui/core/Avatar';
import { Redirect } from 'react-router-dom';
import { getNameInitials } from "../../lib/user";

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
      return <Avatar>{getNameInitials(user.name)}</Avatar>
    }
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
            style={{
              margin: '5px'
            }}
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

Connection.propTypes = {
  user: PropTypes.shape({
    params: PropTypes.shape({
      active: PropTypes.bool,
      avatar: PropTypes.string,
      email: PropTypes.string,
      id: PropTypes.number,
      name: PropTypes.string
    })
  }),
};
