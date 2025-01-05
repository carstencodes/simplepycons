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


class ProbotIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "probot"

    @property
    def original_file_name(self) -> "str":
        return "probot.svg"

    @property
    def title(self) -> "str":
        return "Probot"

    @property
    def primary_color(self) -> "str":
        return "#00B0D8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Probot</title>
     <path d="M12 .04a1.743 1.743 0 0 0-.537 3.401l-.631
 2.579H2.456A2.456 2.456 0 0 0 0 8.476v13.029a2.456 2.456 0 0 0 2.456
 2.456h19.088c1.356 0 2.456-1.1
 2.456-2.456V8.476c0-1.356-1.1-2.456-2.456-2.456h-8.403l-.616-2.575A1.743
 1.743 0 0 0 11.999.04zM3.933 7.881h16.136c1.101 0 1.994.893 1.994
 1.994v10.117a1.994 1.994 0 0 1-1.994 1.994H3.933a1.994 1.994 0 0
 1-1.994-1.994V9.875c0-1.101.893-1.994 1.994-1.994zm3.254 2.312a4.575
 4.575 0 1 0 0 9.15 4.575 4.575 0 0 0 0-9.15zm9.743 0a4.575 4.575 0 1
 0 0 9.15 4.575 4.575 0 0 0 0-9.15zm-9.743 1.07a3.506 3.506 0 1 1 0
 7.011 3.506 3.506 0 0 1 0-7.011zm9.743 0a3.506 3.506 0 1 1 0 7.011
 3.506 3.506 0 0 1 0-7.011zm-9.743 1.663a1.843 1.843 0 1 0 0 3.686
 1.843 1.843 0 0 0 0-3.686zm9.743 0a1.843 1.843 0 1 0 0 3.686 1.843
 1.843 0 0 0 0-3.686zm-6.927 6.5v2.159h.706v-2.159h-.706zm1.077
 0v2.159h.705v-2.159h-.705zm1.076 0v2.159h.706v-2.159h-.706zm1.077
 0v2.159h.706v-2.159h-.706zm1.077.03v2.1a1.08 1.08 0 0 0
 .829-1.049v-.001c0-.51-.354-.937-.829-1.05zm-4.678.028a1.08 1.08 0 0
 0-.731 1.021v.001c0 .474.306.876.731 1.021v-2.043z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/probot/probot/blob/5d29945'''

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
