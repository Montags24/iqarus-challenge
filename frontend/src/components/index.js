const securityForm = [
  {
    title: 'Security risks',
    formName: 'security',
    formEntries: [
      {
        label: 'risk-armed-groups',
        payloadLabel: 'armedGroupsPresence',
        title: 'Presence of armed groups',
        options: ['Present', 'Absent', 'Unknown']
      },
      {
        label: 'risk-report',
        payloadLabel: 'reportOfViolence',
        title: 'Reports of violence or unrest',
        options: ['Confirmed', 'Suspected', 'Not reported']
      },
      {
        label: 'risk-local-enforcement',
        payloadLabel: 'localEnforcementPresence',
        title: 'Law enforcement or military presence',
        options: ['Present', 'Absent', 'Unknown']
      },
      {
        label: 'risk-comments',
        payloadLabel: 'securityRiskComments',
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
        payloadLabel: 'riskToRelief',
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
    formName: 'roads',
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
    formName: 'buildings',
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
    formName: 'utilities',
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

const communicationsForm = [
  {
    title: 'Communications',
    formName: 'communications',
    formEntries: [
      {
        label: 'comms-infrastructure',
        payloadLabel: 'commsInfrastructure',
        title: 'Status of cell towers and internet infrastructure',
        options: ['Fully operational', 'Partly operational', 'Offline']
      },
      {
        label: 'comms-phone-and-internet',
        payloadLabel: 'commsPhoneAndInternet',
        title: 'Reliability of phone and internet connectivity',
        options: [
          'High (consistent signal and bandwidth)',
          'Moderate (intermittent signal and/or reduced bandwidth)',
          'Low (unreliable signal and insufficient bandwidth)'
        ]
      },
      {
        label: 'comms-availablity',
        payloadLabel: 'commsAvailability',
        title: 'Availability of communication devices',
        options: [
          'Abundant (phones, radios, satellite phones)',
          'Limited (some devices available, may not be enough for all teams)',
          'Scarce (very few devices, priority for critical communications only)'
        ]
      },
      {
        label: 'comms-alternative',
        payloadLabel: 'commsAlternative',
        title: 'Alternative communication methods',
        options: ['Satellite phones', 'High-frequency radios', 'None']
      },
      {
        label: 'comms-comments',
        payloadLabel: 'commsComments',
        title: 'Additional Comments',
        textarea: true
      }
    ]
  },
  {
    title: 'Connectivity',
    formName: 'connectivity',
    formEntries: [
      {
        label: 'connect-electricity',
        payloadLabel: 'connectElectricity',
        title: 'Electricity Availability',
        options: [
          'Stable grid supply',
          'Occasional outages, backup available',
          'Unstable grid, reliance on generators'
        ]
      },
      {
        label: 'connect-fuel-availability',
        payloadLabel: 'connectFuelAvailability',
        title: 'Fuel Availability for Generators',
        options: [
          'Sufficient (reliable supply chain)',
          'Limited (supply chain disruptions possible)',
          'Scarce (no reliable supply chain)'
        ]
      },
      {
        label: 'connect-backup-power',
        payloadLabel: 'connectBackupPower',
        title: 'Backup Power Sources',
        options: [
          'Solar panels (available and reliable)',
          'Batteries (available but unreliable)',
          'None'
        ]
      },
      {
        label: 'connect-local-control',
        payloadLabel: 'connectLocalControl',
        title: 'Local Control of Electricity Supply',
        options: [
          'Government-controlled grid',
          'Independent local entities',
          'No local control, dependent on external sources'
        ]
      },
      {
        label: 'connect-comments',
        payloadLabel: 'connectComments',
        title: 'Additional Comments',
        textarea: true
      }
    ]
  }
]

export { securityForm, infrastructureForm, communicationsForm }
