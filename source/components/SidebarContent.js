import React from 'react';
import MaterialTitlePanel from './MaterialTitlePanel';
import PropTypes from 'prop-types';

const styles = {
  sidebar: {
    width: '100px',
    height: '100%',
  },
  sidebarLink: {
    display: 'block',
    padding: '36px 30px',
    color: '#757575',
    textDecoration: 'none',
    fontSize: '20px'
  },
  divider: {
    margin: '8px 30px',
    height: 1,
    backgroundColor: '#757575',
  },
  content: {
    padding: '36px',
    height: '100%',
    backgroundColor: 'white',
  },
};

const SidebarContent = (props) => {
  const style = styles.sidebar;

  return (
    <MaterialTitlePanel title="Menu" style={style}>
      <div style={styles.content}>
        <a href="" style={styles.sidebarLink}>Rotation</a>
        <a href="" style={styles.sidebarLink}>Scaling</a>
        <a href="" style={styles.sidebarLink}>Rotation</a>
        <a href="" style={styles.sidebarLink}>Scaling</a>
        <a href="" style={styles.sidebarLink}>Rotation</a>
        <a href="" style={styles.sidebarLink}>Scaling</a>
        <a href="" style={styles.sidebarLink}>Rotation</a>
        <a href="" style={styles.sidebarLink}>Scaling</a>
        <a href="" style={styles.sidebarLink}>Rotation</a>
        <a href="" style={styles.sidebarLink}>Scaling</a>
      </div>
    </MaterialTitlePanel>
  );
};

SidebarContent.propTypes = {
  style: PropTypes.object,
};


export default SidebarContent;