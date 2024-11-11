from structural.proxy.proxy import Application, Nginx


def run_test():
	app: Application = Application()
	res = app.handle_request("/app/status", "GET")
	print(res)

	app_nginx = Nginx(
		application=app,
		max_allowed_requests=2,
		supported_methods=["GET", "POST"]
	)
	print("Rate limit set to 2 requests per second")
	res = app_nginx.handle_request("/app/status", "GET")
	print(res)
	res = app_nginx.handle_request("/app/status", "GET")
	print(res)
	res = app_nginx.handle_request("/app/status", "GET")
	print(res)
	res = app_nginx.handle_request("/app/status", "GET")
	print(res)


if __name__ == "__main__":
	run_test()
