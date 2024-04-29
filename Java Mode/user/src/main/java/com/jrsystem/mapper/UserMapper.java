package com.jrsystem.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.jrsystem.bean.User;

@Mapper
public interface UserMapper {
	List<User> getAllUsers();
	User getUserById(Long id);
	void insertUser(User user);
	void updateUser(User user);
	void deleteUser(Long id);
}

