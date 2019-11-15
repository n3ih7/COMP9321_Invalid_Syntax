import time
def auth(user_name,pw=None):
	# 命令行输入的封锁时间
	self.block_duration
	# 如果字典中没有这个用户名
	if user_name not in self.user.keys():
		return False,"user doesn't exist"

	# 离线用户登陆
	elif pw == user[user_name]['pw']:
		# 用户目前离线
		if user[user_name]['status'] != 1:
			# 并且不是被封锁，先判断ban time是不是float(即之前被封锁了)，封锁时间是否已过
			if type(user[user_name]['ban timestamp']) == float：
				if time.time() - user[user_name]['ban timestamp'] >= block_duration:
					user[user_name]['status'] = 1
					user[user_name]['active_time'] = time.time()
					user[i.split()[0]]["fail count"] = 0
					return True,"user login successful"
				else:
					return False, "user is blocked, try later"
			else:
				# 用户之前没有被blocked，密码对上，登陆成功
				user[user_name]['status'] = 1
				user[user_name]['active_time'] = time.time()
				user[i.split()[0]]["fail count"] = 0
				return True,"user login successful"
		# 用户目前已经在线，不允许重复登录
		else:
			return False, "user already logged in"
	
	# 用户提供了密码，但是和字典中对不上，fail count加一，并且检查是否已到3次
	# 如果已到3次，状态代码改成3(blocked)，并且ban timestamp更新为现在时间
	if pw != user[user_name]['pw']:
		user[i.split()[0]]["fail count"] += 1
		if user[i.split()[0]]["fail count"] >= 3:
			user[user_name]['status'] = 3
			user[user_name]['ban timestamp'] = time.time()
		return False,"wrong password"

def check_status(user_name):

	# 以下两个用于已经建立连接，和服务器交互中使用
	# 用户已经建立连接，会来到这个if下面，更新活跃时间
	if user[user_name]['status']==1:
		user[user_name]['active_time'] = time.time()
		return True,"online user"

	# 过了一段时间没有活跃状态，用户状态改成2，offline
	if user[user_name]['status']==2:
		return False,"user not logged in, input password"

