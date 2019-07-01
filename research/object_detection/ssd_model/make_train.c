#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define UP_SIZE 320
#define OK_SIZE 320
#define RIGHT_SIZE 320

int main(){
	int up[UP_SIZE] = {0}, ok[OK_SIZE] = {0}, right[RIGHT_SIZE] = {0};
	freopen("train.txt", "w", stdout);
	srand(time(NULL));
	int i = 0;
	int up_flag = 0, ok_flag = 0, right_flag = 0;
	int up_size = 0, ok_size = 0, right_size = 0;
	while(1){
		int x = rand()%3;
		if(x == 0){
			// up
			if(up_flag) continue;
			else{
				while(1){
					int y = rand()%UP_SIZE+1;
					if(up[y] == 0){
						i++;
						up_size++;
						up[y] = 1;
						printf("up_%d\n", y);
						if(up_size == 300) up_flag = 1;
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
					int y = rand()%OK_SIZE+1;
					if(ok[y] == 0){
						i++;
						ok_size++;
						ok[y] = 1;
						printf("ok_%d\n", y);
						if(ok_size == 300) ok_flag = 1;
						break;
					}
				}
			}
		}
		else if(x == 2){
                        // right
                        if(right_flag) continue;
                        else{
                                while(1){
                                        int y = rand()%RIGHT_SIZE+1;
                                        if(right[y] == 0){
                                                i++;
                                                right_size++;
                                                right[y] = 1;
                                                printf("right_%d\n", y);
                                                if(right_size == 300) right_flag = 1;
                                                break;
                                        }
                                }
                        }
                }
		if(up_flag && ok_flag && right_flag) break;
	}
	freopen("val.txt", "w", stdout);
	for(i = 0; i < OK_SIZE; ++i){
		if(ok[i] == 0) printf("ok_%d\n", i+1);
		if(up[i] == 0) printf("up_%d\n", i+1);
		if(right[i] == 0) printf("right_%d\n", i+1);
	}
}
