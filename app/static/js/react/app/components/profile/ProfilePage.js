import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';

class ProfilePage extends React.Component {
  isCurrentUser(profileNumber) {
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
      return <h1>Loading</h1>
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

ProfilePage.propTypes = {
  filter: PropTypes.string,
  onFilter: PropTypes.func,
  match: PropTypes.shape({
    params: PropTypes.shape({
      number: PropTypes.string
    })
  })
};

const mapStateToProps = (state) => {
  return {
    filter: state.filter
  };
};


export default connect(
  mapStateToProps,
)(ProfilePage);
