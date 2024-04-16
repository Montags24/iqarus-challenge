const securityForm = [
  {
    title: 'Security risks',
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
    formEntries: [
      {
        label: 'incidents-reported',
        payloadLabel: 'incidentsReported',
        title: 'Reported Incidents',
        options: ['Looting', 'Theft', 'Vandalism', 'Violence', 'No reported incidents']
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

export { securityForm }
