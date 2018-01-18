
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_NAME_LENGTH 10
#define MAX_STUDENT 5

struct student{
    int id;
    char name[MAX_NAME_LENGTH];
    int score;
};

typedef struct student student_t;


void input(student_t studentList[]);
void studentInfo(student_t studentList[]);
int getMaxID(student_t studentList[]);
int getMaxScore(student_t studentList[]);
char* getMaxName(student_t studentList[]);
int cmpByID(const void *a, const void *b);
void sortByID(student_t* studentList);
int cmpByName(const void *a, const void *b);
void sortByName(student_t* studentList);


int main() {
    student_t *studnetList = malloc(sizeof(student_t) * MAX_STUDENT);
    input(studnetList);
    printf("Student Information:\n\n");
    studentInfo(studnetList);
    printf("\n\n");
    printf("Max ID %d\n",getMaxID(studnetList));
    printf("Max Name %s\n",getMaxName(studnetList));
    printf("Max score %d\n",getMaxScore(studnetList));
    printf("\n\n");
    printf("Sort by ID\n");
    sortByID(studnetList);
    studentInfo(studnetList);
    printf("Sort by Name\n");
    sortByName(studnetList);
    studentInfo(studnetList);
    return 0;
}
void input(student_t studentList[])
{
    int i = 0;
    for(i = 0; i < MAX_STUDENT; i++)
    {
        printf("Please input student name");
        scanf("%s", studentList[i].name);
        printf("Please input student ID");
        scanf("%d", &studentList[i].id);
        printf("Please input student score");
        scanf("%d", &studentList[i].score);
    }
}
void studentInfo(student_t studentList[])
{
    int i = 0;
    printf("ID\t\tName\tScore\t\t\n");
    for(i = 0; i < MAX_STUDENT; i++)
    {
        printf("%d\t\t%s\t\t%d\t\t\n",studentList[i].id, studentList[i].name, studentList[i].score);
    }
}
int getMaxID(student_t studentList[])
{
    int i = 0;
    int MaxId = 0;
    for(i = 0; i < MAX_STUDENT; i++)
    {
        if(MaxId < studentList[i].id)
        {
            MaxId = studentList[i].id;
        }
    }
    return MaxId;
}
int getMaxScore(student_t studentList[])
{
    int i = 0;
    int MaxScore = 0;
    for(i = 0; i < MAX_STUDENT; i++)
    {
        if(MaxScore < studentList[i].score)
        {
            MaxScore = studentList[i].score;
        }
    }
    return MaxScore;
}
char* getMaxName(student_t studentList[])
{
    int i = 0;
    char* MaxName = studentList[0].name;
    for(i = 0; i < MAX_STUDENT; i++)
    {
        if(strcmp(studentList[i].name, MaxName) == 1)
        {
            MaxName = studentList[i].name;
        }
    }
    return MaxName;
}
int cmpByID(const void *a, const void *b)
{
    student_t* tempA = (student_t *) a;
    student_t* tempB = (student_t *) b;
    if(tempA->id != tempB->id)
    {
        return tempA->id > tempB->id ? 1: -1;
    }
    return 0;
}
void sortByID(student_t* studentList)
{
    qsort(studentList, MAX_STUDENT, sizeof(student_t), cmpByID);
}

int cmpByName(const void *a, const void *b)
{
    student_t* tempA = (student_t *) a;
    student_t* tempB = (student_t *) b;
    return strcmp(tempA->name, tempB->name);
}
void sortByName(student_t* studentList)
{
    qsort(studentList, MAX_STUDENT, sizeof(student_t), cmpByName);
}