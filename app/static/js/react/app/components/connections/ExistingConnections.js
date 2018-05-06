import PropTypes from 'prop-types';
import React from 'react';
import { orderBy } from "lodash";

export default class ExistingConnections extends React.Component {
  listConnections(userId, connections) {
    return connections.map((connection) => {
      return this.renderConnection(userId, connection)
    })
  }

  renderConnection(userId, connection) {
    if (userId === connection.user_1.id) {
      return <li key={connection.user_2.id}>{connection.user_2.name}</li>
    } else {
      return <li key={connection.user_1.id}>{connection.user_1.name}</li>
    }
  }

  renderCurrentConnection(userId, connection) {
    if (connection) {
      return (
        <div>
          <h3>Current Connection</h3>
          <ul>{this.renderConnection(userId, connection)}</ul>
        </div>
      )
    }
  }

  render() {
    if (this.props.userDetails) {
      const sortedConnections = orderBy(this.props.userDetails.connections, ['id'], ['desc']);
      const currentConnection = sortedConnections.shift();
      return (
        <div>
          {this.renderCurrentConnection(this.props.userDetails.id, currentConnection)}
          <ul>{this.listConnections(this.props.userDetails.id, this.props.userDetails.connections)}</ul>
        </div>
      )
    } else {
      return (
        <div></div>
      )
    }
  }
}

ExistingConnections.propTypes = {
  userDetails: PropTypes.object
};

