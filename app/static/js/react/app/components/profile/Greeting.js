import PropTypes from 'prop-types';
import React from 'react';
import {isCurrentUser} from "../../lib/user";

export default class Greeting extends React.Component {

  renderGreeting() {
    if (this.props.userDetails) {
      if (isCurrentUser(this.props.userID)) {
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

