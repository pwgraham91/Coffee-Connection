import PropTypes from 'prop-types';
import React from 'react';

export default class GenerateConnections extends React.Component {
  constructor(props) {
    super(props)
    this.onClickGenerateConnections = this.onClickGenerateConnections.bind(this)
  }
  onClickGenerateConnections() {
    const onGeneration = this.props.onGeneration
    fetch(
      '/api/connections/generate_connections',
      {
        method: 'POST',
        credentials: 'include',
      }
    )
    .then(response => response.json())
    .then(data => {
      onGeneration(data)
    })
  }

  render() {
    return (
      <div>
        <button onClick={this.onClickGenerateConnections}>Generate Connections</button>
      </div>
    )
  }
}

GenerateConnections.propTypes = {
  userDetails: PropTypes.object,
  onGeneration: PropTypes.func
};

