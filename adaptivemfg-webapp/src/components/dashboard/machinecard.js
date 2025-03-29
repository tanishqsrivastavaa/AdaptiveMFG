import React from 'react';

const MachineCard = ({ machine }) => {
  return (
    <div className="machine-card">
      <h3>{machine.name}</h3>
      <p>Status: {machine.status}</p>
    </div>
  );
};

export default MachineCard;
