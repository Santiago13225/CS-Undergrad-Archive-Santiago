import java.util.*;//Imports ArrayList, which is used to store the tasks in the scheduling queue.

public class Priority implements Algorithm {//Priority class implements the Algorithm interface and its methods.

    private List<Task> queue;//We declare a private List instance variable called queue that represents the queue of tasks to be executed.

    public Priority(List<Task> queue) {//The Priority constructor takes in a list of tasks.
        this.queue = queue;//Initializes the queue instance variable with the passed list of tasks.
    }
    
    // Invokes the scheduler
    public void schedule(){
        System.out.println("Starting Priority Scheduler");
        while (!queue.isEmpty()) {//While the queue is not empty.
            Task nextTask = pickNextTask();//pickNextTask() picks the next task from the queue based on the Priority algorithm.
            CPU.run(nextTask, nextTask.getBurst());//Simulates the execution of a task on a CPU. 
        }
        System.out.println("Priority Scheduler Finished");
    }

    // Selects the next task using the appropriate scheduling algorithm
    public Task pickNextTask(){
        Task nextTask = queue.get(0);//Retrieves the first task in the queue, which is the one with the highest priority since Priority scheduling selects the task with the highest priority value first. 

        for (Task t : queue) {//For each task in the queue.
            if (t.getPriority() < nextTask.getPriority()) {//Select task with lowest numerical number.
                nextTask = t;
            }
        }
        queue.remove(nextTask);//Removes the nextTask from the queue list.
        return nextTask;//Returns the next task.
    }
}

/*
import java.util.List;//Imports ArrayList, which is used to store the tasks in the scheduling queue.

public class Priority implements Algorithm {//Priority class implements the Algorithm interface and its methods.

    private List<Task> queue;//We declare a private List instance variable called queue that represents the queue of tasks to be executed.

    public Priority(List<Task> queue) {//The Priority constructor takes in a list of tasks.
        this.queue = queue;//Initializes the queue instance variable with the passed list of tasks.
    }

    // Invokes the scheduler
    public void schedule(){
        System.out.println("Starting Priority Scheduler");
        while (!queue.isEmpty()) {//While the queue is not empty.
            Task nextTask = pickNextTask();//pickNextTask() picks the next task from the queue based on the Priority algorithm.
            CPU.run(nextTask, nextTask.getBurst());//Simulates the execution of a task on a CPU.
        }
        System.out.println("Priority Scheduler Finished");
    }

    // Selects the next task using the appropriate scheduling algorithm
    public Task pickNextTask(){
        Task nextTask = queue.get(0);//Retrieves the first task in the queue, which is the one with the highest priority since Priority scheduling selects the task with the highest priority value first. 

        for (Task t : queue) {//For each task in the queue.
            if (t.getPriority() > nextTask.getPriority()) {//Select task with lowest numerical number.
                nextTask = t;
            }
        }
        queue.remove(nextTask);//Removes the nextTask from the queue list.
        return nextTask;//Returns the next task.
    }
}
*/