<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

  <!-- Template to match the root element -->
  <xsl:template match="/">
    <html>
      <head>
        <title>Hockey Database</title>
        <style>
          table {border-collapse: collapse; width: 100%;}
          th, td {border: 1px solid black; padding: 8px; text-align: left;}
          th {background-color: #f2f2f2;}
        </style>
      </head>
      <body>
        <h1>Hockey Database - Tables</h1>
        <!-- Iterate over each table -->
        <xsl:for-each select="hockeydb/table">
          <h2>Table: <xsl:value-of select="@name"/></h2>
          <!-- Display column names -->
          <table>
            <thead>
              <tr>
                <xsl:for-each select="column/rowinfo">
                  <th><xsl:value-of select="@name"/></th>
                </xsl:for-each>
              </tr>
            </thead>
            <tbody>
              <!-- Iterate over rows and display row data -->
              <xsl:for-each select="data/row">
                <tr>
                  <xsl:for-each select="rowdata">
                    <td><xsl:value-of select="@value"/></td>
                  </xsl:for-each>
                </tr>
              </xsl:for-each>
            </tbody>
          </table>
        </xsl:for-each>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>
