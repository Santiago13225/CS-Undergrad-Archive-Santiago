#include <linux/init.h>
#include <linux/module.h>
#include <linux/jiffies.h>
#include <linux/kernel.h>
#include <linux/proc_fs.h>
#include <asm/uaccess.h>
#include <asm/param.h>

#define BUFFER_SIZE 128
#define PROC_NAME "seconds"
//#define MESSAGE "seconds, hi? hello?\n"
long int j;

ssize_t proc_read(struct file *file, char *buf, size_t count, loff_t *pos);
//ssize_t proc_read(struct file *file, char __user *usr_buf, size_t count, loff_t *pos);

static struct file_operations proc_ops = {
    .owner = THIS_MODULE,
    .read = proc_read,
};

/* This function is called when the module is loaded. */
static int proc_init(void){
    proc_create(PROC_NAME, 0, NULL, &proc_ops);
    //proc_create(PROC_NAME, 0666, NULL, &proc_ops);
    printk(KERN_INFO "Loading Module\n");
    printk(KERN_INFO "/proc/%s created\n", PROC_NAME);
    //printk(KERN_INFO "Jiffies start: %lu\n", jiffies);
    //printk(KERN_INFO "HZ: %lu\n", HZ);
    j = jiffies;
    return 0;
}

/* This function called when the module is removed. */
static int proc_exit(void){
    remove_proc_entry(PROC_NAME, NULL);
    printk(KERN_INFO "Removing Module\n");
    printk(KERN_INFO "/proc/%s removed\n", PROC_NAME);
    //printk(KERN_INFO "Jiffies end: ", jiffies);
}

ssize_t proc_read(struct file *file, char __user *usr_buf, size_t count, loff_t *pos){
    int rv = 0;
    char buffer[BUFFER_SIZE]
    static int completed = 0;
    if(completed){
        completed = 0;
        return 0;
    }

    completed = 1;
    rv = sprintf(buffer, "Elapsed Seconds Value: %lu\n", (jiffies - j)/HZ);

    copy_to_user(usr_buf, buffer, rv);

    return rv;
}

module_init(proc_init);
module_exit(proc_exit);

MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("Seconds Module");
MODULE_AUTHOR("Santiago A. Bermudez");