#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class LibrariesdotioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "librariesdotio"

    @property
    def original_file_name(self) -> "str":
        return "librariesdotio.svg"

    @property
    def title(self) -> "str":
        return "Libraries.io"

    @property
    def primary_color(self) -> "str":
        return "#337AB7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Libraries.io</title>
     <path d="M3.152
 23.998c-1.164-.054-1.75.044-2.021-.48-.265-.306-.138-3.465-.185-4.694
 1.702-1.365 3.42-2.688 5.145-4.025 0 2.892.147 8.186-.17
 8.72-.27.56-1.33.474-2.77.479zm6.468-.62c-.304-.006-.171-6.048-.204-11.204
 1.704-1.357 3.42-2.678 5.143-4.01-.028 5.924.123 14.775-.108
 15.098-.334.71-1.064.543-2.467.585-1.094-.06-2.058.16-2.364-.469zm8.41.018c-.174-.33-.158-7.898-.104-15.204a500.566
 500.566 0 015.12 3.977c-.027 1.216.103 11.184-.165
 11.18-.28.47-.641.488-2.44.488-.933-.085-1.852.18-2.411-.441zM.979
 15.564C.957 10.754.927 6.047.999
 1.1c.028-.633.251-1.003.94-1.041.538-.07 3.012-.04 3.463.05a.867.867
 0 01.624.65c.097 2.718.075 6.154.097 10.776-1.717 1.341-3.431
 2.678-5.144 4.024zm8.458-6.656c-.048-2.518 0-7.016.03-7.696.077-1.552
 1.087-1.115 2.41-1.2 1.977-.018 2.279.097 2.5.455.246.368.204
 2.598.204 4.422-1.693 1.323-3.594 2.83-5.144
 4.017zm13.583-.013c-1.706-1.338-3.353-2.633-5.064-3.964.015-1.322-.064-2.744.01-3.995.107-.54.257-.836
 1.16-.866 1.118-.122 2.726-.09 3.419.142.524.124.52 1.379.485 5.226z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/librariesio/libraries.io/b
lob/9ab0f659bb7fe137c15cf676612b6811f501a0bd/public/safari-pinned-tab.'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
