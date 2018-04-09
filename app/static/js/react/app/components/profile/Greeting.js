import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';

class Greeting extends React.Component {
  isCurrentUser() {
    return window.user && this.props.match.params.number == window.user.id
  }

  renderGreeting() {
    if (this.state) {
      if (this.isCurrentUser()) {
        return <h1>Hi, {this.state.name}</h1>
      } else {
        return <h1>{this.state.name}</h1>
      }
    } else {
      return <div></div>
    }
  }

  componentDidMount() {
    fetch(`/api/user/${this.props.match.params.number}`)
    .then(response => response.json())
    .then(data => this.setState(data))
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
  userState: PropTypes.object
};

