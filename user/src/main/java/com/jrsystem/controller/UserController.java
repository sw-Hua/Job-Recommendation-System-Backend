package com.jrsystem.controller;

import com.jrsystem.service.UserService;
import com.jrsystem.bean.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/users")
public class UserController {
	@Autowired
	private UserService userService;

	@GetMapping
	public List<User> getAllUsers() {
		return userService.getAllUsers();
	}

	@GetMapping("/{id}")
	public User getUserById(@PathVariable Long id) {
		return userService.getUserById(id);
	}

	@PostMapping
	public void insertUser(@RequestBody User user) {
		userService.insertUser(user);
	}

	@PutMapping("/{id}")
	public void updateUser(@PathVariable Long id, @RequestBody User user) {
		user.setId(id);
		userService.updateUser(user);
	}

	@DeleteMapping("/{id}")
	public void deleteUser(@PathVariable Long id) {
		userService.deleteUser(id);
	}
}