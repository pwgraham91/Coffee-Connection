import PropTypes from 'prop-types';
import React from 'react';
import { orderBy } from "lodash";
import Connection from "./Connection";

export default class ExistingConnections extends React.Component {
  listConnections(userId, connections) {
    return connections.map((connection) => {
      return this.renderConnection(userId, connection)
    })
  }

  renderConnection(userId, connection) {
    if (userId === connection.user_1.id) {
      return <Connection key={connection.user_2.id} user={connection.user_2} />
    } else {
      return <Connection key={connection.user_1.id} user={connection.user_1} />
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

  renderPastConnections(userId, connections) {
    if (connections) {
      return (
        <div>
          <h3>Previous Connections</h3>
          <ul>{this.listConnections(this.props.userDetails.id, this.props.userDetails.connections)}</ul>
        </div>
      )
    }
  }

  render() {
    if (this.props.userDetails) {
      const sortedConnections = orderBy(this.props.userDetails.connections, ['id'], ['desc']);
      console.log('check the sorted connections', sortedConections)
      // todo check that the shift removes the connection
      const currentConnection = sortedConnections.shift();
      return (
        <div>
          {this.renderCurrentConnection(this.props.userDetails.id, currentConnection)}
          {this.renderPastConnections(this.props.userDetails.id, currentConnection)}
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

