const securityForm = [
  {
    title: 'Security risks',
    formName: 'security',
    formEntries: [
      {
        label: 'risk-armed-groups',
        payloadLabel: 'riskArmedGroups',
        title: 'Presence of armed groups',
        options: ['Present', 'Absent', 'Unknown']
      },
      {
        label: 'risk-report',
        payloadLabel: 'riskReport',
        title: 'Reports of violence or unrest',
        options: ['Confirmed', 'Suspected', 'Not reported']
      },
      {
        label: 'risk-local-enforcement',
        payloadLabel: 'riskLocalEnforcement',
        title: 'Law enforcement or military presence',
        options: ['Present', 'Absent', 'Unknown']
      },
      {
        label: 'risk-comments',
        payloadLabel: 'riskComments',
        title: 'Additional Comments',
        textarea: true
      }
    ]
  },
  {
    title: 'Incidents',
    formName: 'incidents',
    formEntries: [
      {
        label: 'incidents-reported',
        payloadLabel: 'incidentsReported',
        title: 'Reported incidents',
        options: ['Looting', 'Theft', 'Vandalism', 'Violence', 'No reported inclabelents']
      },
      {
        label: 'incidents-risk-to-relief',
        payloadLabel: 'incidentsRiskToRelief',
        title: 'Security incidents affecting relief efforts',
        options: ['High risk', 'Moderate risk', 'Low risk', 'Unknown']
      },
      {
        label: 'incidents-comments',
        payloadLabel: 'incidentsComments',
        title: 'Additional Comments',
        textarea: true
      }
    ]
  }
]

const infrastructureForm = [
  {
    title: 'Roads',
    formEntries: [
      {
        title: 'Condition',
        label: 'road-condition',
        payloadLabel: 'roadCondition',
        options: ['Clear', 'Damaged', 'Blocked']
      },
      {
        title: 'Type of damage',
        label: 'road-damage',
        payloadLabel: 'roadDamage',
        options: ['Flooded', 'Debris', 'Collapsed', 'None']
      },
      {
        title: 'Accessibility',
        label: 'road-access',
        payloadLabel: 'roadAccess',
        options: ['Passable', 'Impassable']
      },
      {
        label: 'road-comments',
        payloadLabel: 'roadComments',
        title: 'Additional Comments',
        textarea: true
      }
    ]
  },
  {
    title: 'Buildings',
    formEntries: [
      {
        title: 'Structural Integrity',
        label: 'building-integrity',
        payloadLabel: 'buildingIntegrity',
        options: ['Intact', 'Damaged', 'Collapsed']
      },
      {
        title: 'Type',
        label: 'building-type',
        payloadLabel: 'buildingType',
        options: ['Reslabelential', 'Commercial', 'Government', 'None']
      },
      {
        title: 'Damage Assessment',
        label: 'building-damage',
        payloadLabel: 'buildingDamage',
        options: ['Minor', 'Moderate', 'Severe']
      },
      {
        label: 'building-comments',
        payloadLabel: 'buildingComments',
        title: 'Additional Comments',
        textarea: true
      }
    ]
  },
  {
    title: 'Utilities',
    formEntries: [
      {
        title: 'Power Supply',
        label: 'utility-power',
        payloadLabel: 'utilityPower',
        options: ['Available', 'Outages', 'Generators']
      },
      {
        title: 'Water Supply',
        label: 'utility-water',
        payloadLabel: 'utilityWater',
        options: ['Functional', 'Contaminated', 'Shortages']
      },
      {
        title: 'Communications',
        label: 'utility-comms',
        payloadLabel: 'utilityComms',
        options: ['Functional', 'Cell Service Only', 'Internet Connectivity', 'Limited']
      },
      {
        label: 'utility-comments',
        payloadLabel: 'utilityComments',
        title: 'Additional Comments',
        textarea: true
      }
    ]
  }
]

export { securityForm, infrastructureForm }
