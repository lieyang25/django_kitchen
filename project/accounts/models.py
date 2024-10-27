from django.db import models

# Create your models here.
class Pizza(models.Model):
    """我的披萨"""
    name = models.CharField(max_length=20)  #名称不超过20个字符串
    time_added = models.DateTimeField(auto_now_add=True)    #自动添加时间

    def __str__(self):
        """返回披萨名"""
        return self.name

class Entry(models.Model):
    """披萨配方"""
    #后面那个会在删除Pizza的时候同时删除相关Entry
    topic = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text) > 20:
            return f"{self.text[:35]}..."
        return self.text