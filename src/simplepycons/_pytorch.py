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


class PytorchIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pytorch"

    @property
    def original_file_name(self) -> "str":
        return "pytorch.svg"

    @property
    def title(self) -> "str":
        return "PyTorch"

    @property
    def primary_color(self) -> "str":
        return "#EE4C2C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PyTorch</title>
     <path d="M12.005 0L4.952 7.053a9.865 9.865 0 000 14.022 9.866
 9.866 0 0014.022 0c3.984-3.9 3.986-10.205.085-14.023l-1.744
 1.743c2.904 2.905 2.904 7.634 0 10.538s-7.634 2.904-10.538
 0-2.904-7.634 0-10.538l4.647-4.646.582-.665zm3.568 3.899a1.327 1.327
 0 00-1.327 1.327 1.327 1.327 0 001.327 1.328A1.327 1.327 0 0016.9
 5.226 1.327 1.327 0 0015.573 3.9z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://github.com/pytorch/pytorch.github.io/
blob/381117ec296f002b2de475402ef29cca6c55e209/assets/brand-guidelines/'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/pytorch/pytorch.github.io/'''

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
