# include <iostream>
# include <vector>

int	main(void)
{
	std::vector<int>	v;


	v.push_back(3);
	v.push_back(4);
	v.push_back(5);

	std::cout << "size: " << v.size() << std::endl;	
	std::vector<int>::iterator iter = v.begin();
	while (iter != v.end())
	{
		std::cout << "addr: " << &iter << std::endl;
		std::cout << "value: " << *iter << std::endl; 
		iter++;
	}
	return (EXIT_SUCCESS);
}
