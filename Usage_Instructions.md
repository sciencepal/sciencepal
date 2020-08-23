Usage Instructions

1. Fork this repo
2. Create a new token from here github.com/settings/tokens/new
3. Give repo read write and workflow permissions to the token and store its value
4. Add the token as a repo secret (Settings -> Secret) with key GH_TOKEN_1 and value equal to token value stored above

What this repo does

1. Fetches chess.com results of my last 100 games
2. Creates an Ascii chart of the results
3. Updates the chart
4. Updates workflow file to generate next run interval (1,2,3,...8 hours)
5. Repeats from step 1

NOTE:

To make any changes to workflow, make sure to make change in both .github/workflows/rating-chart.yaml and assets/workflow.txt as assets file is taken for rewrite in next update.
