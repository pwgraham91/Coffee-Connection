import PropTypes from 'prop-types';
import React from 'react';

export default class ExistingConnections extends React.Component {
  listConnections(userDetails) {
    if (!userDetails) {
      return null
    }
    return userDetails.connections.map((connection) => {
      return <li>{connection.user_1.name}</li>
    })
  }

  render() {
    console.log(this.props.userDetails)
    return (
      <div>
        <h1>existing</h1>
        <ul>{this.listConnections(this.props.userDetails)}</ul>
      </div>
    )
  }
}

ExistingConnections.propTypes = {
  userID: PropTypes.string,
  userDetails: PropTypes.object
};

