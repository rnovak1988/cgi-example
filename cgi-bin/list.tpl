<!DOCTYPE html>
<html>
	<head>
		<title>List | All the DB Yo!!</title>
		<link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css" />
		<link rel="stylesheet" type="text/css" href="/css/bootstrap-theme.min.css" />
		<script type="text/javascript" src="/js/jquery-1.11.3.min.js"></script>
		<script type="text/javascript" src="/js/bootstrap.min.js"></script>
		<style type="text/css">
			div.container {
				margin-top:20px;
			}
		</style>
	</head>
	<body>
		<div class="container">
			<div class="panel panel-success">
				<div class="panel-heading">
					<div class="panel-title">
						Database Contents
					</div>
				</div>
				<div class="panel-body">
					<table class="table">
						<thead>
							<tr>
								<th>First Name</th>
								<th>Last Name</th>
								<th>Address 1</th>
								<th>Address 2</th>
								<th>City</th>
								<th>State</th>
							</tr>
						</thead>
						<tbody>
							%%TBODY-START%%
							%%TBODY-END%%
						</tbody>
					</table>
					<div class="btn-group btn-group-justified" role="group">
						<a href="/" class="btn btn-primary">Home</a>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>
