import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';

export default class Greeting extends React.Component {
  isCurrentUser() {
    return window.user && parseInt(this.props.userID) === parseInt(window.user.id)
  }

  renderGreeting() {
    if (this.props.userDetails) {
      if (this.isCurrentUser()) {
        return <h1>Hi, {this.props.userDetails.name}</h1>
      } else {
        return <h1>{this.props.userDetails.name}</h1>
      }
    } else {
      return <div></div>
    }
  }

  render() {
    const greeting = this.renderGreeting();
    return (
      <div>
        {greeting}
      </div>
    )
  }
}

Greeting.propTypes = {
  userID: PropTypes.string,
  userDetails: PropTypes.object
};

