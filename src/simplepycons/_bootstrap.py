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


class BootstrapIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bootstrap"

    @property
    def original_file_name(self) -> "str":
        return "bootstrap.svg"

    @property
    def title(self) -> "str":
        return "Bootstrap"

    @property
    def primary_color(self) -> "str":
        return "#7952B3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bootstrap</title>
     <path d="M11.77 11.24H9.956V8.202h2.152c1.17 0 1.834.522 1.834
 1.466 0 1.008-.773 1.572-2.174 1.572zm.324
 1.206H9.957v3.348h2.231c1.459 0 2.232-.585
 2.232-1.685s-.795-1.663-2.326-1.663zM24
 11.39v1.218c-1.128.108-1.817.944-2.226 2.268-.407 1.319-.463
 2.937-.42 4.186.045 1.3-.968 2.5-2.337 2.5H4.985c-1.37
 0-2.383-1.2-2.337-2.5.043-1.249-.013-2.867-.42-4.186-.41-1.324-1.1-2.16-2.228-2.268V11.39c1.128-.108
 1.819-.944 2.227-2.268.408-1.319.464-2.937.42-4.186-.045-1.3.968-2.5
 2.338-2.5h14.032c1.37 0 2.382 1.2 2.337 2.5-.043 1.249.013 2.867.42
 4.186.409 1.324 1.098 2.16 2.226 2.268zm-7.927
 2.817c0-1.354-.953-2.333-2.368-2.488v-.057c1.04-.169 1.856-1.135
 1.856-2.213 0-1.537-1.213-2.538-3.062-2.538h-4.16v10.172h4.181c2.218
 0 3.553-1.086 3.553-2.876z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
