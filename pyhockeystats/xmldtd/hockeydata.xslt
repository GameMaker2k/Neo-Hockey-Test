<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

  <!-- Template to match the root element -->
  <xsl:template match="/">
    <html>
      <head>
        <title>Hockey Data</title>
        <style>
          table {border-collapse: collapse; width: 100%;}
          th, td {border: 1px solid black; padding: 8px; text-align: left;}
          th {background-color: #f2f2f2;}
        </style>
      </head>
      <body>
        <h1>Hockey Leagues</h1>
        <xsl:for-each select="hockey/league">
          <h2>League: <xsl:value-of select="@fullname"/> (<xsl:value-of select="@name"/>)</h2>
          <p>Country: <xsl:value-of select="@fullcountry"/> (Short: <xsl:value-of select="@country"/>)</p>
          <table>
            <thead>
              <tr>
                <th>Conference</th>
                <th>Division</th>
                <th>Team</th>
                <th>City</th>
                <th>Arena</th>
              </tr>
            </thead>
            <tbody>
              <xsl:for-each select="conference">
                <xsl:for-each select="division">
                  <xsl:for-each select="team">
                    <tr>
                      <td><xsl:value-of select="../../@name"/> Conference</td>
                      <td><xsl:value-of select="../@name"/> Division</td>
                      <td><xsl:value-of select="@name"/></td>
                      <td><xsl:value-of select="@city"/></td>
                      <td><xsl:value-of select="@arena"/></td>
                    </tr>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </tbody>
          </table>

          <h3>Games</h3>
          <table>
            <thead>
              <tr>
                <th>Date</th>
                <th>Time</th>
                <th>Home Team</th>
                <th>Away Team</th>
                <th>Goals</th>
                <th>Faceoffs Won</th>
                <th>Penalties</th>
              </tr>
            </thead>
            <tbody>
              <xsl:for-each select="games/game">
                <tr>
                  <td><xsl:value-of select="@date"/></td>
                  <td><xsl:value-of select="@time"/></td>
                  <td><xsl:value-of select="@hometeam"/></td>
                  <td><xsl:value-of select="@awayteam"/></td>
                  <td><xsl:value-of select="@goals"/></td>
                  <td><xsl:value-of select="@faceoffwins"/></td>
                  <td><xsl:value-of select="@penalties"/></td>
                </tr>
              </xsl:for-each>
            </tbody>
          </table>
        </xsl:for-each>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>
