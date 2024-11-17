using Microsoft.AspNetCore.Mvc;

namespace DemoService.Service.Controllers
{
    [ApiController]
    public class WidgetServiceController : WidgetServiceControllerBase
    {
        static WidgetService serviceImpl = new WidgetService();
        internal override IWidgetService WidgetServiceImpl => serviceImpl;
    }
}
