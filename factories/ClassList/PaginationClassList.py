from models.Pagination.CreateFirstPageUrl import CreateFirstPageUrl
from models.Pagination.CreateLastPageUrl import CreateLastPageUrl
from models.Pagination.CreatePrevPageUrl import CreatePrevPageUrl
from models.Pagination.CreateNextPageUrl import CreateNextPageUrl
from models.Pagination.CurrentPage import CurrentPage
from models.Pagination.FromTo import FromTo
from models.Pagination.LastPage import LastPage
from models.Pagination.Paginate.CreateCursor import CreateCursor
from models.Pagination.Paginate.Total import Total
from models.Pagination.PerPage import PerPage
from template_methods.PaginationTemplate import PaginationTemplate

PAGINATION_CLASS_LIST = {
    'PaginationTemplate': PaginationTemplate,
    # 'SearchPaginationTemplate': SearchPaginationTemplate,
    'CreateFirstPageUrl': CreateFirstPageUrl,
    'CreateLastPageUrl': CreateLastPageUrl,
    'CreateNextPageUrl': CreateNextPageUrl,
    'CreatePrevPageUrl': CreatePrevPageUrl,
    # 'CreateOffsetSearch': CreateOffsetSearch,
    'CreateCursor': CreateCursor,
    'Total': Total,
    # 'TotalSearch': TotalSearch,
    'PerPage': PerPage,
    'CurrentPage': CurrentPage,
    'LastPage': LastPage,
    'FromTo': FromTo
}
