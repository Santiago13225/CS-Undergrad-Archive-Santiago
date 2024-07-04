import java.util.*;//Imports ArrayList, which is used to store the tasks in the scheduling queue.

public class SJF implements Algorithm {//SJF class implements the Algorithm interface and its methods.

    private List<Task> queue;//We declare a private List instance variable called queue that represents the queue of tasks to be executed.

    public SJF(List<Task> queue) {//The SJF constructor takes in a list of tasks.
        this.queue = queue;//Initializes the queue instance variable with the passed list of tasks.
    }
    
    // Invokes the scheduler
    public void schedule(){
        // Sort the queue based on burst time
        Collections.sort(queue, new Comparator<Task>() {//Sorts the queue list based on the burst time of each task.
            public int compare(Task task1, Task task2) {//We use a custom Comparator to compare the burst times of two tasks.
                return task1.getBurst() - task2.getBurst();
                /*^If task1 has a shorter burst time than task2, compare returns a negative number, indicating that task1 
                should come before task2 in the sorted queue. If task1 has a longer burst time than task2, compare returns 
                a positive number, indicating that task1 should come after task2 in the sorted queue. If task1 and task2 
                have the same burst time, compare returns 0, indicating that their relative order in the queue doesn't 
                matter.*/
            }
        });
        // Execute tasks in the sorted order
        for (Task task : queue) {//After sorting, we execute the tasks in the order of their burst times using a for-each loop.
            CPU.run(task, task.getBurst());//Simulates the execution of a task on a CPU. 
            /*^It takes two arguments: task is the task to be executed, and task.getBurst() returns the amount of time the task 
            requires to complete its execution.*/
        }
    }

    // Selects the next task using the appropriate scheduling algorithm
    public Task pickNextTask(){
        // This method is not needed for SJF, since all tasks are executed in the order of their burst time
        return null;
    }

}