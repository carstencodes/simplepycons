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


class UberIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "uber"

    @property
    def original_file_name(self) -> "str":
        return "uber.svg"

    @property
    def title(self) -> "str":
        return "Uber"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Uber</title>
     <path d="M0 7.97v4.958c0 1.867 1.302 3.101 3 3.101.826 0
 1.562-.316 2.094-.87v.736H6.27V7.97H5.082v4.888c0 1.257-.85
 2.106-1.947 2.106-1.11 0-1.946-.827-1.946-2.106V7.971H0zm7.44
 0v7.925h1.13v-.725c.521.532 1.257.86 2.06.86a3.006 3.006 0 0 0
 3.034-3.01 3.01 3.01 0 0 0-3.033-3.024 2.86 2.86 0 0
 0-2.049.861V7.971H7.439zm9.869 2.038c-1.687 0-2.965 1.37-2.965 3 0
 1.72 1.334 3.01 3.066 3.01 1.053 0 1.913-.463
 2.49-1.233l-.826-.611c-.43.577-.996.847-1.664.847-.973
 0-1.753-.7-1.912-1.64h4.697v-.373c0-1.72-1.222-3-2.886-3zm6.295.068c-.634
 0-1.098.294-1.381.758v-.713h-1.131v5.774h1.142V12.61c0-.894.544-1.47
 1.291-1.47H24v-1.065h-.396zm-6.319.928c.85 0 1.564.588 1.756
 1.47H15.52c.203-.882.916-1.47 1.765-1.47zm-6.732.012c1.086 0 1.98.883
 1.98 2.004a1.993 1.993 0 0 1-1.98 2.001A1.989 1.989 0 0 1 8.56
 13.02a1.99 1.99 0 0 1 1.992-2.004z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://assets.uber.com/d/k4nuxdZ8MC7E/user-g'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://assets.uber.com/d/k4nuxdZ8MC7E/logos/'''

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
