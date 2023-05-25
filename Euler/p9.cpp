#include <cmath>
#include <iostream>

// Fast bruteforce on c++


bool is_triplet(int a, int b, int c)
{
	if ((a*a + b*b == c*c) && (a+b+c == 1000))
		return true;
	return false;
}

int bruteforce_triplet()
{
	for(int a = 1; a < 1000; a++)
		for(int b = 1; b < 1000; b++)
			for(int c = 1; c < 1000; c++)
				if (is_triplet(a, b, c))
				{
					std::cout << a << " " << b << " "  << c << std::endl;
					return a * b * c;
				}
}

void main()
{
	std::cout << bruteforce_triplet() << std::endl;
}