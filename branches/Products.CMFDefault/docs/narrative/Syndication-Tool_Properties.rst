SyndicationTool - Properties: Manage the properties of a Site's Syndication Instance
====================================================================================

Description
-----------

View and manage the properties of a sitewide syndication instance.

Controls
--------

**Enable/Disable Syndication** --
  Turns enables/disables sitewide syndication. All methods check whether site
  syndication is enabled to ensure a sitewide policy is enforceable.

**Syndication Module** --
  The RSS sy XMLNS is supported in this tool by default. The following
  properties are editable on the tool for sitewide configuring of each of the
  elements of the syndication module. In this release, they are
  over-rideable; these will be configurable in version 1.1 to enable a
  sitewide policy.

**UpdatePeriod** --
  Describes the period over which the channel format is updated. Acceptable
  values are: hourly, daily, weekly, monthly, yearly. If omitted, daily is
  assumed.

**UpdateFrequency** --
  Used to describe the frequency of updates in relation to the update period. A
  positive integer indicates how many times in that period the channel is
  updated. For example, an updatePeriod of daily, and an updateFrequency of 2
  indicates the channel format is updated twice daily. If omitted a value of 1
  is assumed

**UpdateBase** --
  Defines a base date to be used in concert with updatePeriod and
  updateFrequency to calculate the publishing schedule. By default the
  sitewide date is the DateTime of the tool initialization. The UpdateBase in
  the RSS XML takes this DateTime object and sringify's it through
  DateTime.HTML4() The date format takes the form: yyyy-mm-ddThh:mm

**Max Items** --
  Defines the max number of items which are included in the syndication. The
  RSS Specification recommends this not exceed 15, which is the default.

**DublinCore Module** --
  The RSS dc XMLNS is supported in this tool by default. The sitewide
  properties will be editable on the tool for sitewide configuring of each of
  the elements of the dublin core module. In this release, they are
  over-rideable; these will be configurable in version 1.1 to
  enable a sitewide policy.
