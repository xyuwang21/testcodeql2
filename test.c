#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void example1() {
    int *ptr = NULL;

    // 存空指针引用
    *ptr = 10;  // 错误：尝试解引用空指针

    printf("Value: %d\n", *ptr);
}

void example2() {
    int *ptr = (int *)malloc(sizeof(int));
    if (ptr == NULL) {
        printf("Memory allocation failed\n");
        return;
    }

    *ptr = 20;  // 使用分配的内存
    printf("Value before free: %d\n", *ptr);

    // 释放指针后使用
    free(ptr);
    printf("Value after free: %d\n", *ptr);  // 错误：使用已经释放的内存
}

void example3() {
    // 内存泄漏示例
    char *str = (char *)malloc(100 * sizeof(char));  // 分配100个字符大小的内存
    if (str == NULL) {
        printf("Memory allocation failed\n");
        return;
    }

    strcpy(str, "Hello, world!");  // 将字符串复制到分配的内存
    printf("String: %s\n", str);

    // 内存泄漏：没有调用 free 释放内存
    // 忘记释放内存，导致无法回收分配的内存
}

void example4() {
    // 字符串复制少零符示例
    char source[] = "Hello";
    char dest[6];  // 分配了6个字符的空间，正好适合存储 "Hello" 和 '\0'

    // 错误：未正确复制 '\0'，导致目标字符串未终止
    strncpy(dest, source, 5);  // 只复制5个字符，不包括 '\0'
    
    // 由于 dest 没有 '\0' 终止符，这会导致后续字符串处理出错
    printf("Dest string: %s\n", dest);  // 未定义行为，可能不会打印正确的内容
}

int main() {
    //example1();  // 存空指针引用示例
    example2();  // 指针释放后使用示例
    example3();  // 内存泄漏示例
    example4();  // 字符串复制少零符示例

    return 0;
}
