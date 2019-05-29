#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define UP_SIZE 240
#define OK_SIZE 220

int main(){
	int up[UP_SIZE] = {0}, ok[OK_SIZE] = {0};
	freopen("train.txt", "w", stdout);
	srand(time(NULL));
	int i = 0;
	int up_flag = 0, ok_flag = 0;
	int up_size = 0, ok_size = 0;
	while(1){
		int x = rand()%2;
		if(x == 0){
			// up
			if(up_flag) continue;
			else{
				while(1){
					int y = rand()%UP_SIZE;
					if(up[y] == 0){
						i++;
						up_size++;
						up[y] = 1;
						if(y < 10) printf("up_00%d\n", y);
						else if(y < 100) printf("up_0%d\n", y);
						else printf("up_%d\n", y);
						if(up_size == 200) up_flag = 1;
						break;
					}
				}
			}
		}
		else if(x == 1){
			// down
			if(ok_flag) continue;
			else{
				while(1){
					int y = rand()%OK_SIZE;
					if(ok[y] == 0){
						i++;
						ok_size++;
						ok[y] = 1;
						if(y < 10) printf("ok_00%d\n", y);
						else if(y < 100) printf("ok_0%d\n", y);
						else printf("ok_%d\n", y);
						if(ok_size == 200) ok_flag = 1;
						break;
					}
				}
			}
		}
		if(up_flag && ok_flag) break;
	}
}
