import java.util.*;//Imports ArrayList, which is used to store the tasks in the scheduling queue.

public class FCFS implements Algorithm {//FCFS class implements the Algorithm interface and its methods.

    private List<Task> queue;//We declare a private List instance variable called queue that represents the queue of tasks to be executed.

    public FCFS(List<Task> queue) {//The FCFS constructor takes in a list of tasks.
        this.queue = queue;//Initializes the queue instance variable with the passed list of tasks.
    }

    // Invokes the scheduler
    public void schedule(){
        while (!queue.isEmpty()) {//While the queue is not empty.
            Task task = pickNextTask();//Repeatedly select and execute the next task until the queue is empty.
            /*^pickNextTask() selects the next task from the queue based on the FCFS algorithm, which simply 
            removes the first task in the queue and returns it.*/ 
            //CPU.run(task, task.getBurstTime());
            CPU.run(task, task.getBurst());//Simulates the execution of a task on a CPU.
            /*^It takes two arguments: task is the task to be executed, and task.getBurst() returns the amount of time the task 
            requires to complete its execution.*/
        }
    }

    // Selects the next task using the appropriate scheduling algorithm
    public Task pickNextTask(){
        return queue.remove(0);//Removes and returns the first task from the queue list.
    }
}