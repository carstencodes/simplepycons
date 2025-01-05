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


class HumbleBundleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "humblebundle"

    @property
    def original_file_name(self) -> "str":
        return "humblebundle.svg"

    @property
    def title(self) -> "str":
        return "Humble Bundle"

    @property
    def primary_color(self) -> "str":
        return "#CC2929"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Humble Bundle</title>
     <path d="M17.895 19.341c-3.384 0 1.826-19.186
 1.826-19.186L16.233.151s-1.427 4.515-2.37
 9.533h-3.005c.078-1.032.116-2.076.099-3.114-.135-8.26-4.974-6.73-7.14-4.835C1.758
 3.538.033 6.962 0 9.6c.328-.016 1.624-.022 1.624-.022S2.702 4.66
 6.086 4.66c3.385 0-1.834 19.187-1.834 19.187l3.49.002s1.803-5.136
 2.7-10.872l2.87-.017c-.167 1.485-.22 3.124-.196 4.646.136 8.26 4.956
 6.488 7.122 4.593 2.166-1.896 3.782-5.9
 3.762-7.822.002-.002-1.645.013-1.665.013.006.152-1.056 4.951-4.44
 4.951z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://support.humblebundle.com/hc/en-us/art'''

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
